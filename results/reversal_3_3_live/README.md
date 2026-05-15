# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 15:15:04 EDT`
Last processed slot: `manual`

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
- Equity: `$30,995.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 14875.0        29.05          29.75       350.6         347.7          bid_ask_mid                      29.75                bid_ask_mid                    True           350.0                   2.41          97.3               37              0.63         45.67           50.93                  37.94                2023.0           40.0               0.13                      ok
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
  NXPI           82.86               35            0.53              1.09        293.70                90.16         0.727          pass              0.566             83.4                           0.594               -0.89              0.049                                 ok            True                  False
   TXN           91.30               23            1.23              2.66        307.03                67.99         0.687          pass              0.655             65.9                           0.520                8.86              1.051                                 ok            True                  False
 GOOGL           82.61               23            1.23              3.44        399.60                40.65         0.564          pass              0.341             42.6                           0.432                2.71              0.314                                 ok            True                  False
  GOOG           83.33               24            1.19              3.30        395.75                40.76         0.563          pass              0.362             41.1                           0.433                2.41              0.303                                 ok            True                  False
  SNPS           95.83               24            1.81              6.46        507.25                41.57         0.530          pass              0.700             51.4                           0.419                2.41              0.286                                 ok            True                  False
  CDNS           96.43               28            1.50              3.70        351.26                37.94         0.527          pass              0.651             26.3                           0.199                1.94              0.163                                 ok            True                  False
  MPWR           83.33               18            2.53             28.56       1601.73                52.07         0.511          pass              0.301             35.9                           0.471               -0.65              0.157                                 ok            True                  False
   WMT           95.00               20            0.92              0.85        132.09                21.34         0.507          pass              0.599             27.2                           0.384               -0.08              0.072                                 ok            True                  False
  MDLZ           82.61               23            0.83              0.35         60.82                21.64         0.500          pass              0.282             25.2                           0.259               -1.47             -0.088                                 ok            True                  False
 CMCSA           90.00               10            1.57              0.28         25.05                60.26         0.707          pass              0.355              6.0                           0.158               -8.88             -1.001 downtrend_blocked_slope_and_streak           False                  False
  INTC          100.00                3            5.88              4.77        113.88               111.79         0.601          pass              0.554             31.2                           0.430                9.53              1.667                                 ok           False                  False
  FTNT           97.92               48            0.02              0.01        121.85                71.29         0.581          pass              0.957             99.5                           0.626               41.20              3.925                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-15T15:10:01.306366-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T15:05:04.259285-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T15:00:04.164689-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T14:55:04.243758-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-15T14:50:02.185201-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T14:50:02.185201-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-15", "training_samples": 5061, "window": 5}
2026-05-15T12:00:02.263118-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:55:05.834638-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:50:01.284692-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-15T11:45:04.258436-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515151504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515151504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515151504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515151504)

</details>
