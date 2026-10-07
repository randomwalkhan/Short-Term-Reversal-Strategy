# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-07 15:40:05 EDT`
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

- Cash: `$734.30`
- Equity: `$107,609.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$2,462.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   1     55     52112.5                 54175.0         9.48           9.85      160.14        160.42          bid_ask_mid                       9.85                bid_ask_mid                    True          2062.5                   3.96         83.33               12              2.40         42.26           44.20                  40.56                 310.0           20.0               0.06                      ok
  NVDA     option         option NVDA261120C00235000       2026-10-07                   0     40     52300.0                 52700.0        13.08          13.18      236.83        236.94          bid_ask_mid                      13.18                bid_ask_mid                    True           400.0                   0.76         90.91               22              1.01         37.07           37.07                  24.15               17037.0         1205.0               0.01                      ok
```

## Today's Closed Trades (2026-10-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.48               27            3.34              3.84        162.61               111.15         0.663          pass              0.391             57.2                           0.841                8.56              1.311                                 ok            True                  False
  MPWR           84.21               19            2.80             28.89       1461.31                53.62         0.534          pass              0.323             32.4                           0.704                5.83              0.963                                 ok            True                  False
  NVDA           91.30               23            0.96              1.61        238.55                24.15         0.509          pass              0.498             19.6                           0.395                5.07              0.672                                 ok            True                  False
  UPRO           85.19               27            0.93              1.02        155.97                30.90         0.509          pass              0.472             56.4                           0.466                3.09              0.346                                 ok            True                  False
   ADI           83.33               12            2.57              7.57        417.30                32.72         0.509          pass              0.249             32.1                           0.710                6.36              0.907                                 ok            True                  False
  DASH           82.14               28            1.61              2.18        192.69                42.81         0.501          pass              0.322             31.5                           0.256                0.66              0.206                                 ok            True                  False
  META           58.33               12            2.40             12.39        733.57                55.45         0.569          pass              0.081              3.4                           0.089               -3.08             -0.348            downtrend_blocked_slope           False                  False
   STX           88.24               34            0.84              4.74        803.60                69.91         0.564          pass              0.654             72.6                           0.684              -13.46             -1.291            downtrend_blocked_slope           False                  False
  QCOM           84.00               25            2.06              2.61        179.91                56.22         0.547          pass              0.364             34.3                           0.573              -10.11             -1.079 downtrend_blocked_slope_and_streak           False                  False
   CEG           86.11               36            0.49              1.03        299.96                58.89         0.543          pass              0.659             89.5                           0.704               13.28              1.074                                 ok           False                  False
   KDP           85.71                7            1.81              0.40         30.96                26.61         0.541          pass              0.206              0.0                           0.155               -3.06             -0.232                                 ok           False                  False
  SNPS           82.50               40            0.44              1.56        504.50                54.22         0.533          pass              0.512             63.9                           0.597               21.76              2.341                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-07T15:10:05.672351-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:05:05.765684-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:00:04.880221-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:55:05.726912-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:50:06.730595-04:00       entry_1500                   entry {"allocated_cash": 52300.0, "asset_type": "option", "contract_symbol": "NVDA261120C00235000", "contracts": 40, "early_entry_score": 0.461, "entry_mode": "regular", "entry_option_price": 13.075, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 17037.0, "option_spread_pct": 1.15, "option_volume": 1205.0, "success_rate": 90.91, "ticker": "NVDA", "timing_score": 0.512}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                 {"early_entry_score": 0.14, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.522}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                   {"early_entry_score": 0.49, "option_liquidity_status": "low_volume", "option_open_interest": 993.0, "option_spread_pct": 12.24, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.545}
2026-10-07T14:50:06.730595-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-07", "training_samples": 5970, "window": 5}
2026-10-07T12:00:04.521112-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T11:55:05.517664-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261007154005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261007154005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261007154005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261007154005)

</details>
