# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 11:25:01 EDT`
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
  TEAM           90.48               42            0.86              0.51         85.20               109.49         0.670          pass              0.782             78.5                           0.597               -3.01              0.040                      ok            True                   True
  MELI           92.31               26            1.45             16.87       1657.19                60.80         0.591          pass              0.643             49.7                           0.663                5.33              0.700                      ok            True                  False
  ASML           87.88               33            0.90             10.25       1628.51                54.77         0.569          pass              0.458             12.4                           0.111                3.35              0.360                      ok            True                  False
  PAYX           90.91               11            1.26              0.86         96.63                28.52         0.554          pass              0.527             57.9                           0.696                3.33              0.598                      ok            True                  False
   ADP           93.33               15            1.95              3.07        223.99                37.70         0.546          pass              0.511             22.6                           0.493                4.37              0.660                      ok            True                  False
   ROP           84.62               13            1.85              4.23        325.13                26.18         0.525          pass              0.218              7.5                           0.175               -2.40              0.041                      ok            True                  False
  CTSH           89.29               28            1.13              0.42         52.57                46.65         0.520          pass              0.611             63.9                           0.681                6.65              1.339                      ok            True                  False
  ROST           94.12               34            0.55              0.90        234.42                38.50         0.505          pass              0.781             64.7                           0.559                8.84              0.768                      ok            True                   True
 CMCSA           84.21               19            1.03              0.18         25.13                20.74         0.503          pass              0.330             35.8                           0.341               -0.34              0.025                      ok            True                  False
  CSCO           80.00                5            2.23              1.88        119.60                52.25         0.641          pass              0.121             18.9                           0.347               19.25              1.866                      ok           False                  False
  INTU           78.57               14            3.63              8.12        316.46                90.56         0.628          pass              0.118              9.7                           0.224              -21.60             -2.284 downtrend_blocked_slope           False                  False
   TRI           73.33               15            1.28              0.77         85.53                55.00         0.626          pass              0.252             52.2                           0.445               -4.28              0.108                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                  detail
2026-05-26T11:25:01.332906-04:00 early_entry_1125 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:20:01.352478-04:00 early_entry_1120 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:15:02.326421-04:00 early_entry_1115 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:10:05.334078-04:00 early_entry_1110 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:05:05.735209-04:00 early_entry_1105 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T11:00:04.326254-04:00 early_entry_1100 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:55:01.312359-04:00 early_entry_1055 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:50:01.303434-04:00 early_entry_1050 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-26T10:50:01.303434-04:00      manage_1100          exit {"asset_type": "option", "contract_symbol": "TTWO260717C00230000", "fill_price": 11.35, "pnl": 2325.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.82, "ticker": "TTWO"}
2026-05-26T10:50:01.303434-04:00      manage_1100          exit      {"asset_type": "option", "contract_symbol": "SBUX260717C00105000", "fill_price": 3.2625, "pnl": -1377.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SBUX"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526112501)

</details>
