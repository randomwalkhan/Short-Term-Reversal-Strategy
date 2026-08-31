# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-31 10:10:04 EDT`
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

- Cash: `$50,178.10`
- Equity: `$50,178.10`
- Realized PnL: `$40,178.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-31)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SHOP     option         option SHOP261016C00155000     29          2026-08-28         2026-08-31          9.0         8.1 -2610.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  MNST           81.82               11            1.56              0.51         46.64               551.82         1.000          pass              0.208             17.7                           0.178                1.34              0.008                  ok            True                  False
  ABNB          100.00               13            2.09              2.77        188.24                62.79         0.682          pass              0.514              8.6                           0.152                3.45              0.291                  ok            True                  False
   TRI           93.10               29            1.16              0.86        105.85                60.45         0.590          pass              0.762             75.8                           0.653                6.68              0.431                  ok            True                  False
  MELI          100.00               24            1.48             20.34       1957.53                48.83         0.589          pass              0.654             33.8                           0.464                8.37              0.822                  ok            True                  False
  PAYX          100.00               17            0.97              0.86        126.67                24.67         0.579          pass              0.555             16.8                           0.177                6.13              0.600                  ok            True                  False
  MSTR           85.37               41            0.53              0.48        127.11                81.68         0.578          pass              0.551             50.0                           0.339               29.64              3.316                  ok            True                  False
  SBUX           95.00               20            0.71              0.54        107.62                22.68         0.544          pass              0.632             36.9                           0.433               -0.78              0.151                  ok            True                  False
  VRTX           96.88               32            0.71              2.71        540.53                33.03         0.533          pass              0.777             59.1                           0.659                4.32              0.293                  ok            True                  False
 CMCSA           93.75               16            1.55              0.29         26.93                25.33         0.528          pass              0.488              9.7                           0.187                4.18              0.347                  ok            True                  False
  UPRO           84.21               19            1.58              1.68        151.06                30.93         0.518          pass              0.224              0.0                           0.221               -3.25             -0.102                  ok            True                  False
  BKNG           95.00               20            1.89              2.72        204.47                35.32         0.517          pass              0.615             32.3                           0.482               -1.47             -0.241                  ok            True                  False
  CHTR           90.62               32            1.60              1.72        152.88                53.40         0.516          pass              0.550             22.6                           0.250                4.90              0.373                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-31T10:10:04.381634-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-31T10:05:01.432627-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "entry_ask": 24.9, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 21.65, "hypothetical_budget": 25089.05, "hypothetical_contracts": 11, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 39.0, "option_spread_pct": 30.02, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.804, "early_reclaim_pct": 64.0, "matched_signals": 34, "recovery_stability_score": 0.675, "success_rate": 97.06, "ticker": "VRTX", "timing_score": 0.526, "trend_health_status": "ok"}, {"current_drop_pct": 1.13, "early_entry_score": 0.777, "early_reclaim_pct": 76.3, "matched_signals": 30, "recovery_stability_score": 0.634, "success_rate": 93.33, "ticker": "TRI", "timing_score": 0.586, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-31T10:00:05.270470-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-31T09:50:01.420574-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "SHOP261016C00155000", "fill_price": 8.1, "pnl": -2610.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SHOP"}
2026-08-31T03:00:02.021557-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 93}
2026-08-29T02:55:05.202083-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:50:05.132580-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:45:01.295429-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:40:01.326395-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
2026-08-29T02:35:05.989284-04:00   share_ext_0235      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260831101004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260831101004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260831101004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260831101004)

</details>
