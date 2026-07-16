# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 10:15:01 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   ADI     option         option ADI260821C00380000      4          2026-07-15         2026-07-16        35.15      31.635 -1406.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  META           82.61               23            1.35              6.45        678.54                54.55         0.599          pass              0.347             43.5                           0.450                9.66              1.347                                 ok            True                  False
   ADI           84.00               25            1.58              4.31        389.11                55.85         0.588          pass              0.425             53.3                           0.752               -3.11              0.041                                 ok            True                  False
   TXN           85.71               14            3.10              6.53        298.39                65.52         0.582          pass              0.300             21.0                           0.375               -2.08              0.140                                 ok            True                  False
  UPRO           86.67               30            0.53              0.54        145.64                41.96         0.565          pass              0.572             68.0                           0.770                2.33              0.294                                 ok            True                  False
  NXPI           85.71               21            2.40              4.68        277.00                58.07         0.562          pass              0.370             29.5                           0.566               -3.10              0.129                                 ok            True                  False
   WBD           89.47               19            0.64              0.12         27.22                20.00         0.524          pass              0.608             81.1                           0.477                1.63              0.254                                 ok            True                  False
  AVGO           81.82               22            2.37              6.55        391.47                51.57         0.515          pass              0.307             42.4                           0.740                1.90              0.691                                 ok            True                  False
  BKNG           85.19               27            1.24              1.58        182.12                43.83         0.513          pass              0.361             19.3                           0.147                1.29             -0.225                                 ok            True                  False
  SOXL           85.00               20            7.45              8.64        161.85               219.49         0.715          pass              0.396             41.4                           0.718              -42.56             -3.401            downtrend_blocked_slope           False                  False
  LRCX           88.89               27            1.00              2.35        334.42                98.70         0.702          pass              0.659             79.6                           0.836              -23.37             -1.791 downtrend_blocked_slope_and_streak           False                  False
    MU           80.95               21            3.24             20.52        895.49               112.73         0.680          pass              0.301             44.6                           0.717              -24.19             -1.578            downtrend_blocked_slope           False                  False
  MSTR           70.59               34            2.07              1.41         96.86               100.18         0.633          pass              0.363             46.4                           0.676                9.80              0.339                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-16T10:15:01.181570-04:00 early_entry_1015      early_entry_shadow {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "entry_ask": 15.35, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 14.1, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 42, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 17.73, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.786, "shadow_only": true, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.871, "early_reclaim_pct": 75.3, "matched_signals": 42, "recovery_stability_score": 0.786, "success_rate": 97.62, "ticker": "FTNT", "timing_score": 0.454, "trend_health_status": "ok"}, {"current_drop_pct": 0.73, "early_entry_score": 0.754, "early_reclaim_pct": 77.6, "matched_signals": 41, "recovery_stability_score": 0.827, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:10:01.416514-04:00 early_entry_1010      early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.5, "early_entry_score": 0.884, "early_reclaim_pct": 79.9, "entry_ask": 15.6, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 10, "matched_signals": 44, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 19.33, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.725, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.884, "early_reclaim_pct": 79.9, "matched_signals": 44, "recovery_stability_score": 0.725, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:05:04.361041-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.92, "early_entry_score": 0.817, "early_reclaim_pct": 63.4, "entry_ask": 16.05, "entry_bid": 13.4, "entry_mode": "early", "entry_option_price": 14.725, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 627.0, "option_spread_pct": 18.0, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.56, "shadow_only": true, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.817, "early_reclaim_pct": 63.4, "matched_signals": 37, "recovery_stability_score": 0.56, "success_rate": 97.3, "ticker": "FTNT", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-16T10:00:05.335836-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T10:00:05.335836-04:00      manage_1000                    exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "ADI260821C00380000", "fill_price": 31.635, "pnl": -1406.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "ADI"}
2026-07-15T15:10:01.366399-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-15T15:05:02.437789-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-15T15:00:06.972520-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-07-15T14:50:07.762689-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"allocated_cash": 14060.0, "asset_type": "option", "contract_symbol": "ADI260821C00380000", "contracts": 4, "early_entry_score": 0.523, "entry_mode": "regular", "entry_option_price": 35.15, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 129.0, "option_spread_pct": 5.41, "option_volume": 42.0, "success_rate": 86.21, "ticker": "ADI", "timing_score": 0.569}
2026-07-15T14:50:07.762689-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"early_entry_score": 0.633, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 14.0, "option_spread_pct": 5.41, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.636}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716101501)

</details>
