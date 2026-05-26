# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 11:30:01 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$31,585.25`
- Equity: `$31,585.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26       30.350     36.1500  2320.0   19.110379 take_profit_day2_hit_at_scan
  SBUX     option         option SBUX260717C00105000     38          2026-05-22         2026-05-26        3.625      3.2625 -1377.5  -10.000000        stop_loss_hit_at_scan
  TTWO     option         option TTWO260717C00230000     15          2026-05-26         2026-05-26        9.800     11.3500  2325.0   15.816327 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           90.91               44            0.52              0.31         85.29               109.49         0.679          pass              0.820             87.0                           0.688               -2.67              0.055                      ok            True                   True
  MELI           92.31               26            1.37             16.02       1657.56                60.80         0.596          pass              0.651             52.3                           0.688                5.41              0.703                      ok            True                  False
  ASML           87.88               33            0.83              9.45       1628.85                54.77         0.574          pass              0.478             19.2                           0.125                3.42              0.363                      ok            True                  False
  PAYX           92.31               13            1.19              0.81         96.65                28.52         0.546          pass              0.584             60.2                           0.709                3.40              0.602                      ok            True                  False
   ADP           93.33               15            2.03              3.21        223.94                37.70         0.541          pass              0.501             19.2                           0.400                4.28              0.656                      ok            True                  False
   ROP           83.33               12            1.87              4.29        325.10                26.18         0.529          pass              0.173              6.1                           0.163               -2.43              0.040                      ok            True                  False
  AMGN           84.00               25            0.67              1.59        338.62                27.24         0.524          pass              0.305             15.5                           0.350                3.03              0.224                      ok            True                  False
  CTSH           89.29               28            1.13              0.42         52.57                46.65         0.520          pass              0.611             63.9                           0.698                6.65              1.339                      ok            True                  False
  CSCO           80.00                5            2.12              1.78        119.65                52.25         0.648          pass              0.134             23.1                           0.370               19.39              1.872                      ok           False                  False
   TRI           73.33               15            1.18              0.71         85.56                55.00         0.633          pass              0.265             56.1                           0.598               -4.18              0.112                      ok           False                  False
  INTU           78.57               14            3.69              8.27        316.40                90.56         0.623          pass              0.113              8.0                           0.240              -21.65             -2.287 downtrend_blocked_slope           False                  False
  SBUX           92.31               13            1.22              0.88        102.73                33.02         0.608          pass              0.546             45.6                           0.394               -3.11             -0.265 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                  detail
2026-05-26T11:30:01.341956-04:00 early_entry_1130 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:25:01.332906-04:00 early_entry_1125 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:20:01.352478-04:00 early_entry_1120 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:15:02.326421-04:00 early_entry_1115 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:10:05.334078-04:00 early_entry_1110 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:05:05.735209-04:00 early_entry_1105 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:00:04.326254-04:00 early_entry_1100 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:55:01.312359-04:00 early_entry_1055 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:50:01.303434-04:00 early_entry_1050 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:50:01.303434-04:00      manage_1100          exit {"asset_type": "option", "contract_symbol": "TTWO260717C00230000", "fill_price": 11.35, "pnl": 2325.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.82, "ticker": "TTWO"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526113001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526113001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526113001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526113001)

</details>
