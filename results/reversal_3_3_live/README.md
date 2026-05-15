# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-15 13:25:05 EDT`
Last processed slot: `manage_1330`

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
- Equity: `$31,345.00`
- Realized PnL: `$20,645.00`
- Unrealized PnL: `$700.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CDNS     option         option CDNS260618C00330000       2026-05-15                   0      5     14525.0                 15225.0        29.05          30.45       350.6        350.16          bid_ask_mid                      30.45                bid_ask_mid                    True           700.0                   4.82          97.3               37              0.63         45.67           48.25                  37.94                2023.0           40.0               0.13                      ok
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
   TXN           93.75               32            0.56              1.22        307.65                67.99         0.675          pass              0.834             84.4                           0.776                9.60              1.082                                 ok            True                   True
  GOOG           85.71               28            0.95              2.63        396.04                40.76         0.555          pass              0.487             53.1                           0.597                2.66              0.314                                 ok            True                  False
 GOOGL           85.71               28            0.96              2.71        399.91                40.65         0.551          pass              0.492             54.8                           0.622                2.98              0.326                                 ok            True                  False
  SNPS           96.00               25            1.76              6.28        507.33                41.57         0.527          pass              0.711             52.7                           0.599                2.46              0.288                                 ok            True                  False
  CDNS           97.30               37            0.58              1.44        352.22                37.94         0.524          pass              0.846             71.2                           0.680                2.89              0.205                                 ok            True                   True
   LIN           84.21               19            1.23              4.42        509.75                21.81         0.502          pass              0.224              0.4                           0.193               -0.51              0.204                                 ok            True                  False
  NXPI           84.21               38            0.28              0.58        293.92                90.16         0.725          pass              0.645             91.2                           0.746               -0.64              0.060                                 ok           False                  False
 CMCSA           88.89               18            0.89              0.16         25.10                60.26         0.703          pass              0.424             21.1                           0.296               -8.26             -0.970 downtrend_blocked_slope_and_streak           False                  False
  GEHC           46.67               15            2.12              0.93         62.27                57.53         0.593          pass              0.143             16.9                           0.433                0.51              0.181                                 ok           False                  False
  INTC          100.00                2            6.27              5.09        113.75               111.79         0.585          pass              0.538             26.6                           0.543                9.07              1.649                                 ok           False                  False
   XEL          100.00                1            2.54              1.42         79.42                24.20         0.579          pass              0.462              1.5                           0.161               -5.55             -0.376            downtrend_blocked_slope           False                  False
  CHTR           66.67                3            6.16              6.38        145.27               114.29         0.571          pass              0.078              7.0                           0.193              -19.13             -1.819            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                            detail
2026-05-15T12:00:02.263118-04:00 early_entry_1200 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:55:05.834638-04:00 early_entry_1155 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:50:01.284692-04:00 early_entry_1150 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:45:04.258436-04:00 early_entry_1145 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:40:01.250267-04:00 early_entry_1140 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:35:04.114840-04:00 early_entry_1135 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:30:01.141517-04:00 early_entry_1130 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:25:04.096857-04:00 early_entry_1125 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-05-15T11:20:04.254442-04:00      manage_1130          exit {"asset_type": "option", "contract_symbol": "SNPS260618C00490000", "fill_price": 40.23, "pnl": -1341.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-15T11:20:04.254442-04:00 early_entry_1120 entry_skipped                                                                                                                                                   {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260515132505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260515132505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260515132505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260515132505)

</details>
