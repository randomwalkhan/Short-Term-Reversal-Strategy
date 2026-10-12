# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-12 15:35:02 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$1,059.30`
- Equity: `$121,354.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$4,080.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option  CEG261120C00290000       2026-10-12                   0     31     57815.0                 60295.0        18.65          19.45      291.07        292.61          bid_ask_mid                      19.45                bid_ask_mid                    True          2480.0                   4.29         83.33               12              2.35         48.77           48.31                  62.49                 920.0          121.0               0.05                      ok
  CTSH     option         option CTSH261120C00060000       2026-10-09                   1    160     58400.0                 60000.0         3.65           3.75       59.31         59.64          bid_ask_mid                       3.75                bid_ask_mid                    True          1600.0                   2.74         93.10               29              1.17         50.42           52.93                  46.57                 209.0           38.0               0.08                      ok
```

## Today's Closed Trades (2026-10-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           91.18               34            1.24              1.34        153.76                79.86         0.604            pass              0.654             45.1                           0.522               -3.00             -0.233                                 ok            True                  False
    ZS           84.62               13            3.25              5.31        231.45                75.53         0.528            pass              0.245             16.5                           0.384               13.42              1.597                                 ok            True                  False
   CEG           85.00               20            1.85              3.85        296.42                62.49         0.527            pass              0.338             28.3                           0.535               12.34              1.682                                 ok            True                  False
  ABNB           82.61               23            1.43              1.66        165.16                38.25         0.522            pass              0.294             28.5                           0.468                4.75              0.446                                 ok            True                  False
  SNPS           72.22               18            1.68              6.01        507.42                55.08         0.600            pass              0.151             12.6                           0.220               20.07              2.020                                 ok           False                  False
  QCOM           90.32               31            0.64              0.78        175.16                55.68         0.598            pass              0.674             66.5                           0.648               -6.99             -0.694 downtrend_blocked_slope_and_streak           False                  False
   STX           86.36               22            3.12             17.10        775.67                69.65         0.532            pass              0.376             24.4                           0.602              -17.68             -2.255            downtrend_blocked_slope           False                  False
  CSCO           60.00                5            2.19              1.81        117.61                33.46         0.532            pass              0.171             39.2                           0.634                8.91              1.152                                 ok           False                  False
   WDC           75.86               29            2.05              5.69        394.84                64.73         0.523            pass              0.265             28.7                           0.666              -14.14             -1.817            downtrend_blocked_slope           False                  False
 CMCSA           91.30               23            0.05              0.01         20.66                20.79         0.519            pass              0.721             93.7                           0.828               -3.76             -0.345            downtrend_blocked_slope           False                  False
  INTC           80.00               20            3.20              2.35        103.69                69.66         0.509            pass              0.166             16.0                           0.526              -12.65             -1.462 downtrend_blocked_slope_and_streak           False                  False
  UPRO           86.49               37            0.24              0.27        155.61                29.53         0.488 below_threshold              0.569             55.8                           0.509                4.43              0.617                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-10-12T15:10:05.555878-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-12T15:05:06.325460-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-12T15:00:05.898503-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-12T14:55:06.164837-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-10-12T14:50:02.373216-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"allocated_cash": 57815.0, "asset_type": "option", "contract_symbol": "CEG261120C00290000", "contracts": 31, "early_entry_score": 0.18, "entry_mode": "regular", "entry_option_price": 18.65, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 920.0, "option_spread_pct": 4.83, "option_volume": 121.0, "success_rate": 83.33, "ticker": "CEG", "timing_score": 0.545}
2026-10-12T14:50:02.373216-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-12", "training_samples": 6005, "window": 5}
2026-10-12T12:00:04.227731-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T11:55:04.380745-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T11:50:05.333973-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-12T11:45:05.208038-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "TTWO261120C00210000", "current_drop_pct": 1.13, "early_entry_score": 0.683, "early_reclaim_pct": 65.0, "entry_ask": 15.4, "entry_bid": 14.6, "entry_mode": "early", "entry_option_price": 15.0, "hypothetical_budget": 29437.15, "hypothetical_contracts": 19, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 800.0, "option_spread_pct": 5.33, "option_volume": 56.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 90.91, "ticker": "TTWO", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 1.13, "early_entry_score": 0.683, "early_reclaim_pct": 65.0, "matched_signals": 33, "recovery_stability_score": 0.749, "success_rate": 90.91, "ticker": "TTWO", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261012153502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261012153502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261012153502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261012153502)

</details>
