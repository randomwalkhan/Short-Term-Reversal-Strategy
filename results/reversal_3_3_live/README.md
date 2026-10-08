# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 09:45:03 EDT`
Last processed slot: `manual`

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
- Equity: `$102,209.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$-2,937.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   2     55     52112.5                 54175.0         9.48           9.85      160.14        162.96     last_price_stale                        NaN                unavailable                   False          2062.5                   3.96         83.33               12              2.40         42.26            0.00                  40.56                 310.0           20.0               0.06                      ok
  NVDA     option         option NVDA261120C00235000       2026-10-07                   1     40     52300.0                 47300.0        13.08          11.82      236.83        234.23          bid_ask_mid                      11.82                bid_ask_mid                    True         -5000.0                  -9.56         90.91               22              1.01         37.07           38.18                  24.15               17037.0         1205.0               0.01                      ok
```

## Today's Closed Trades (2026-10-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           92.50               40            0.53              0.79        213.21                73.23         0.637          pass              0.797             66.8                           0.588               -1.03              0.509                                 ok            True                   True
  MPWR           88.00               25            1.79             17.86       1418.33                55.22         0.566          pass              0.435             21.8                           0.276                5.02              0.843                                 ok            True                  False
  CSCO           88.46               26            0.77              0.63        117.12                34.80         0.554          pass              0.492             34.8                           0.530                9.32              1.195                                 ok            True                  False
   ADI           84.21               19            1.50              4.30        408.24                34.70         0.533          pass              0.306             26.8                           0.350                5.57              0.702                                 ok            True                  False
  AVGO           81.25               16            2.14              5.64        374.09                34.55         0.510          pass              0.147              7.6                           0.256                5.17              0.710                                 ok            True                  False
  UPRO           85.19               27            0.93              1.01        154.79                30.53         0.507          pass              0.452             49.8                           0.660                2.53              0.416                                 ok            True                  False
  QCOM           87.50               24            1.38              1.71        176.39                56.66         0.604          pass              0.470             38.8                           0.478              -10.08             -1.085 downtrend_blocked_slope_and_streak           False                  False
  MSTR           88.89               18            3.59              3.86        151.72                80.80         0.581          pass              0.351              0.7                           0.086               -8.51             -0.249           downtrend_blocked_streak           False                  False
   STX           89.66               29            2.14             12.12        802.37                69.74         0.544          pass              0.496             19.3                           0.278              -12.77             -1.577            downtrend_blocked_slope           False                  False
   WDC           80.00               30            1.66              4.72        403.40                65.89         0.543          pass              0.253             21.8                           0.299              -11.47             -1.384            downtrend_blocked_slope           False                  False
  AMGN           78.57               14            1.33              3.85        411.43                28.61         0.539          pass              0.093              4.0                           0.116                0.38             -0.231                                 ok           False                  False
  SOXL           79.17               24            5.53              6.15        156.23               112.38         0.535          pass              0.200             17.7                           0.454                2.56              0.976                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-08T00:00:04.872922-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 91, 'empty': 2}
2026-10-07T15:10:05.672351-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:05:05.765684-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T15:00:04.880221-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:55:05.726912-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-07T14:50:06.730595-04:00       entry_1500                   entry {"allocated_cash": 52300.0, "asset_type": "option", "contract_symbol": "NVDA261120C00235000", "contracts": 40, "early_entry_score": 0.461, "entry_mode": "regular", "entry_option_price": 13.075, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 17037.0, "option_spread_pct": 1.15, "option_volume": 1205.0, "success_rate": 90.91, "ticker": "NVDA", "timing_score": 0.512}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                 {"early_entry_score": 0.14, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.522}
2026-10-07T14:50:06.730595-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                   {"early_entry_score": 0.49, "option_liquidity_status": "low_volume", "option_open_interest": 993.0, "option_spread_pct": 12.24, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.545}
2026-10-07T14:50:06.730595-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-07", "training_samples": 5970, "window": 5}
2026-10-07T12:00:04.521112-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008094503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008094503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008094503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008094503)

</details>
