# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 10:10:05 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           94.59               37            0.50              0.56        158.37               104.19         0.733            pass              0.894             83.7                           0.533               15.24              2.501                                 ok            True                  False
   CEG           86.96               23            1.10              2.03        262.40                41.90         0.553            pass              0.468             46.8                           0.519               -1.59              0.034                                 ok            True                  False
  UPRO           85.00               20            1.45              1.54        151.54                32.02         0.514            pass              0.307             18.5                           0.319                2.93              0.578                                 ok            True                  False
  PYPL           90.91               22            1.22              0.47         54.84                60.08         0.508            pass              0.626             68.1                           0.773                0.63              0.098                                 ok            True                  False
  MPWR           83.33               24            2.13             20.38       1358.69                54.48         0.505            pass              0.366             44.5                           0.295               17.06              2.166                                 ok            True                  False
  MSFT          100.00               14            1.70              6.14        513.54                25.07         0.501            pass              0.588             37.1                           0.618                0.39              0.215                                 ok            True                  False
  NXPI           85.19               27            1.23              2.05        237.20                39.27         0.500 below_threshold              0.486             61.6                           0.378                5.34              0.669                                 ok            True                  False
   TRI           87.50               32            1.18              0.82         98.64                56.74         0.573            pass              0.563             53.0                           0.600               -7.56             -0.521 downtrend_blocked_slope_and_streak           False                  False
  AMGN           87.50               40            0.09              0.26        414.50                46.27         0.567            pass              0.726             89.7                           0.496                8.58              1.118                                 ok           False                  False
   WBD           95.35               43            0.05              0.01         30.86                38.15         0.559            pass              0.899             81.0                           0.530                9.77              1.280                                 ok           False                  False
  LRCX           76.47               34            1.28              2.83        314.00                61.39         0.533            pass              0.418             68.1                           0.430               13.89              1.820                                 ok           False                  False
  SHOP           73.33               15            3.16              3.15        140.90                62.03         0.502            pass              0.149             21.7                           0.437                2.88              1.074                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-28T10:10:05.010808-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:05:05.986578-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.89, "early_entry_score": 0.731, "early_reclaim_pct": 78.9, "entry_ask": 11.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 9.95, "hypothetical_budget": 34999.15, "hypothetical_contracts": 35, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 35.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.871, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.497, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.731, "early_reclaim_pct": 78.9, "matched_signals": 33, "recovery_stability_score": 0.871, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.497, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:00:06.220548-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T09:50:05.886543-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "MSTR261120C00160000", "fill_price": 15.9975, "pnl": -3555.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-28T03:00:06.642645-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-09-26T02:55:04.179839-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:50:05.866610-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:45:06.222669-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:40:05.820539-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:35:05.219756-04:00   share_ext_0235      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928101005)

</details>
