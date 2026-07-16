# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 09:30:04 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$16,570.25`
- Equity: `$30,462.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$-168.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   ADI     option         option ADI260821C00380000       2026-07-15                   1      4     14060.0                 13892.0        35.15          34.73      388.76        383.24     last_price_stale                        NaN                unavailable                   False          -168.0                  -1.19         86.21               29              1.02          62.6             0.0                  55.85                 129.0           42.0               0.05                      ok
```

## Today's Closed Trades (2026-07-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           88.89               18            2.49              5.25        298.94                65.52         0.599          pass              0.449             33.0                           0.459               -1.47              0.169                                 ok            True                  False
   ADI           86.96               23            1.88              5.15        388.75                55.85         0.585          pass              0.463             44.2                           0.499               -3.42              0.026                                 ok            True                  False
  CSCO           95.24               21            1.18              0.92        111.37                36.51         0.582          pass              0.560              9.6                           0.251               -5.62              0.037                                 ok            True                  False
  NXPI           84.00               25            1.69              3.30        277.60                58.07         0.580          pass              0.408             47.7                           0.434               -2.39              0.162                                 ok            True                  False
  UPRO           86.67               30            0.68              0.69        145.63                41.96         0.558          pass              0.527             53.5                           0.721                2.22              0.289                                 ok            True                  False
  AVGO           80.95               21            2.41              6.66        391.43                51.57         0.534          pass              0.189             12.3                           0.361                1.86              0.690                                 ok            True                  False
  KLAC           84.00               25            1.81              2.84        223.28               109.33         0.726          pass              0.448             56.3                           0.616              -26.94             -2.109 downtrend_blocked_slope_and_streak           False                  False
  SOXL           85.00               20            7.94              9.20        161.58               219.49         0.698          pass              0.368             32.7                           0.780              -42.87             -3.425            downtrend_blocked_slope           False                  False
  AMAT           83.33               18            2.71             11.01        574.71                98.89         0.671          pass              0.327             39.2                           0.546              -22.03             -1.502 downtrend_blocked_slope_and_streak           False                  False
    MU           80.95               21            3.42             21.62        895.01               112.73         0.671          pass              0.291             41.7                           0.636              -24.32             -1.586            downtrend_blocked_slope           False                  False
  MSTR           70.59               34            2.02              1.38         96.88               100.18         0.648          pass              0.308             27.8                           0.433                9.86              0.342                                 ok           False                  False
  ASML           94.12               34            0.44              5.55       1812.89                66.00         0.644          pass              0.849             82.8                           0.705               -9.15             -0.628                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-15T15:10:01.366399-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-15T15:05:02.437789-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-15T15:00:06.972520-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-15T14:50:07.762689-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"allocated_cash": 14060.0, "asset_type": "option", "contract_symbol": "ADI260821C00380000", "contracts": 4, "early_entry_score": 0.523, "entry_mode": "regular", "entry_option_price": 35.15, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 129.0, "option_spread_pct": 5.41, "option_volume": 42.0, "success_rate": 86.21, "ticker": "ADI", "timing_score": 0.569}
2026-07-15T14:50:07.762689-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.633, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 14.0, "option_spread_pct": 5.41, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.636}
2026-07-15T14:50:07.762689-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-15", "training_samples": 5408, "window": 5}
2026-07-15T12:00:03.706415-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "CRWD260821C00210000", "current_drop_pct": 0.92, "early_entry_score": 0.692, "early_reclaim_pct": 65.6, "entry_ask": 14.6, "entry_bid": 14.25, "entry_mode": "early", "entry_option_price": 14.425, "hypothetical_budget": 15315.13, "hypothetical_contracts": 10, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1292.0, "option_spread_pct": 2.43, "option_volume": 518.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.726, "shadow_only": true, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.692, "early_reclaim_pct": 65.6, "matched_signals": 39, "recovery_stability_score": 0.726, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-15T11:55:06.679355-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:50:02.876804-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:45:04.888686-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716093004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716093004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716093004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716093004)

</details>
