# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 14:55:04 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$16,120.00`
- Equity: `$31,295.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$650.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15175.0        29.05          30.35       350.6        348.81          bid_ask_mid                      30.35                bid_ask_mid                    True           650.0                   4.48          97.3               37              0.63         45.67           50.34                  37.94                2023.0           40.0               0.13                      ok
```

## Today's Closed Trades (2026-05-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-14         2026-05-15        32.35      29.115 -1617.5       -10.0 stop_loss_hit_at_scan
  SNPS     option         option SNPS260618C00490000      3          2026-05-13         2026-05-15        44.70      40.230 -1341.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           92.86               28            0.76              1.64        307.47                67.99         0.686          pass              0.769             79.1                           0.611                9.38              1.073                                 ok            True                  False
  GOOG           84.00               25            1.12              3.12        395.83                40.76         0.562          pass              0.396             44.5                           0.361                2.48              0.306                                 ok            True                  False
 GOOGL           83.33               24            1.17              3.29        399.66                40.65         0.562          pass              0.374             45.2                           0.371                2.77              0.316                                 ok            True                  False
  SNPS           96.15               26            1.50              5.36        507.72                41.57         0.535          pass              0.739             59.6                           0.645                2.73              0.300                                 ok            True                  False
  MPWR           88.46               26            1.63             18.36       1606.10                52.07         0.519          pass              0.561             58.8                           0.687                0.27              0.199                                 ok            True                  False
  CDNS           96.97               33            1.12              2.77        351.65                37.94         0.517          pass              0.739             44.8                           0.321                2.33              0.181                                 ok            True                  False
  NXPI           85.00               40            0.13              0.27        294.06                90.16         0.723          pass              0.693             95.9                           0.696               -0.49              0.067                                 ok           False                  False
 CMCSA           90.00               10            1.57              0.28         25.05                60.26         0.707          pass              0.348              3.7                           0.156               -8.88             -1.001 downtrend_blocked_slope_and_streak           False                  False
  INTC          100.00                8            5.17              4.20        114.13               111.79         0.611          pass              0.580             39.5                           0.569               10.36              1.702                                 ok           False                  False
  GEHC           46.67               15            2.23              0.98         62.25                57.53         0.587          pass              0.132             13.4                           0.353                0.40              0.176                                 ok           False                  False
   XEL          100.00                3            2.34              1.31         79.47                24.20         0.573          pass              0.519             20.4                           0.469               -5.35             -0.366            downtrend_blocked_slope           False                  False
  INSM           30.00               10            4.32              3.49        114.12               110.45         0.551          pass              0.153             32.6                           0.573              -16.98             -2.311 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-15T14:55:04.243758-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T14:50:02.185201-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T14:50:02.185201-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-15", "training_samples": 5061, "window": 5}
2026-05-15T12:00:02.263118-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:55:05.834638-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:50:01.284692-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:45:04.258436-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:40:01.250267-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:35:04.114840-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:30:01.141517-04:00 early_entry_1130  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515145504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515145504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515145504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515145504)

</details>
