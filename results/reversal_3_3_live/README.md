# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 10:00:03 EDT`
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

- Cash: `$47,804.30`
- Equity: `$106,241.80`
- Realized PnL: `$89,916.80`
- Unrealized PnL: `$6,325.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   2     55     52112.5                 58437.5         9.48          10.62      160.14        162.99          bid_ask_mid                      10.62                bid_ask_mid                    True          6325.0                  12.14         83.33               12               2.4         42.26           45.99                  40.56                 310.0           20.0               0.06                      ok
```

## Today's Closed Trades (2026-10-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  NVDA     option         option NVDA261120C00235000     40          2026-10-07         2026-10-08       13.075     11.7675 -5230.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           85.00               20            2.32             23.13       1416.07                55.22         0.558          pass              0.337             27.2                           0.285                4.45              0.818                                 ok            True                  False
  AMGN           80.00               15            1.23              3.56        411.56                28.61         0.539          pass              0.151             21.1                           0.214                0.48             -0.226                                 ok            True                  False
   ADI           83.33               18            1.62              4.66        408.08                34.70         0.531          pass              0.258             20.7                           0.219                5.44              0.697                                 ok            True                  False
  AVGO           84.62               13            2.46              6.47        373.74                34.55         0.511          pass              0.221              8.8                           0.181                4.82              0.696                                 ok            True                  False
  UPRO           83.33               30            0.66              0.71        154.85                30.53         0.502          pass              0.464             63.7                           0.706                2.77              0.426                                 ok            True                  False
  MSTR           89.29               28            2.32              2.49        152.30                80.80         0.591          pass              0.536             36.3                           0.533               -7.30             -0.190           downtrend_blocked_streak           False                  False
  CSCO           88.89               27            0.44              0.36        117.24                34.80         0.568          pass              0.596             62.9                           0.706                9.69              1.210                                 ok           False                  False
  META           84.21               38            0.22              1.09        720.84                52.76         0.562          pass              0.613             86.1                           0.423               -7.44             -0.403            downtrend_blocked_slope           False                  False
  QCOM           86.96               23            2.24              2.78        175.93                56.66         0.558          pass              0.369             13.5                           0.261              -10.87             -1.125 downtrend_blocked_slope_and_streak           False                  False
   WDC           81.58               38            0.80              2.26        404.45                65.89         0.547          pass              0.471             62.5                           0.624              -10.69             -1.344            downtrend_blocked_slope           False                  False
   STX           86.67               30            2.02             11.40        802.69                69.74         0.539          pass              0.465             33.4                           0.378              -12.65             -1.571            downtrend_blocked_slope           False                  False
 CMCSA           91.30               23            0.07              0.01         20.94                21.76         0.520          pass              0.717             92.3                           0.703               -3.98             -0.332            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                     detail
2026-10-08T10:00:03.810887-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T09:50:06.393850-04:00      manage_1000                    exit                                                                        {"asset_type": "option", "contract_symbol": "NVDA261120C00235000", "fill_price": 11.7675, "pnl": -5230.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "NVDA"}
2026-10-08T00:00:04.872922-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                  {'saved': 91, 'empty': 2}
2026-10-07T15:10:05.672351-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:05:05.765684-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:00:04.880221-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:55:05.726912-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.14, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.522}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped                   {"early_entry_score": 0.49, "option_liquidity_status": "low_volume", "option_open_interest": 993.0, "option_spread_pct": 12.24, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.545}
2026-10-07T14:50:06.730595-04:00       entry_1500          timing_overlay                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-07", "training_samples": 5970, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008100003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008100003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008100003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008100003)

</details>
