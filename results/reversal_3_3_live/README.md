# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 14:35:04 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$32,264.25`
- Equity: `$32,264.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0      -10.00        stop_loss_hit_at_scan
  AVGO     option         option AVGO260717C00420000      4          2026-05-28         2026-05-28        31.25      35.950  1880.0       15.04 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.86               28            0.54              0.46        119.47                51.65         0.625          pass              0.711             62.0                           0.541               16.84              0.883                                 ok            True                  False
  INTC           96.97               33            0.96              0.82        121.42                92.16         0.622          pass              0.851             78.6                           0.671                0.25              0.784                                 ok            True                   True
  MNST           90.48               21            1.20              0.75         88.92                49.17         0.561          pass              0.500             30.5                           0.477                2.61              0.233                                 ok            True                  False
   WBD           84.21               19            0.57              0.11         27.09                 8.45         0.506          pass              0.249              8.8                           0.304               -0.97             -0.044                                 ok            True                  False
   LIN           88.24               17            1.34              4.78        505.82                20.85         0.502          pass              0.396             26.5                           0.297               -2.38             -0.050                                 ok            True                  False
  MELI           93.18               44            0.02              0.20       1696.09                61.41         0.597          pass              0.906             98.2                           0.417                8.57              0.876                                 ok           False                  False
   XEL          100.00                9            1.77              1.00         80.57                25.49         0.573          pass              0.511             17.8                           0.263               -0.43              0.196                                 ok           False                  False
   AEP           71.43                7            1.43              1.29        129.02                25.33         0.565          pass              0.197             46.7                           0.274               -0.18              0.201                                 ok           False                  False
  AMAT           88.89               36            0.21              0.66        447.97                50.47         0.540          pass              0.736             90.6                           0.463                2.58              0.426                                 ok           False                  False
  ROST           75.00                4            3.10              5.07        231.30                38.54         0.530          pass              0.062              3.0                           0.196                6.83              1.110                                 ok           False                  False
  REGN           88.24               34            0.70              3.09        626.42                48.81         0.516          pass              0.510             26.4                           0.306              -13.28             -1.313 downtrend_blocked_slope_and_streak           False                  False
  LRCX           90.00               40            0.32              0.72        318.62                56.04         0.512          pass              0.788             89.9                           0.702                7.60              1.169                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                  detail
2026-05-28T12:40:01.998163-04:00      manage_1230          exit {"asset_type": "option", "contract_symbol": "AVGO260717C00420000", "fill_price": 35.95, "pnl": 1880.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.04, "ticker": "AVGO"}
2026-05-28T12:00:05.896854-04:00 early_entry_1200 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:55:02.040011-04:00 early_entry_1155 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:50:05.974356-04:00 early_entry_1150 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:45:05.997889-04:00 early_entry_1145 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:40:03.231101-04:00 early_entry_1140 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:35:03.979729-04:00 early_entry_1135 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:30:01.953912-04:00 early_entry_1130 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:25:06.570222-04:00 early_entry_1125 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
2026-05-28T11:20:04.888168-04:00 early_entry_1120 entry_skipped                                                                                                                                                         {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528143504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528143504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528143504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528143504)

</details>
