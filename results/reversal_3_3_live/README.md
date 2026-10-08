# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 09:30:06 EDT`
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

- Cash: `$734.30`
- Equity: `$108,109.30`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$2,962.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ABNB     option         option ABNB261120C00160000       2026-10-06                   2     55     52112.5                 54175.0         9.48           9.85      160.14        161.58     last_price_stale                        NaN                unavailable                   False          2062.5                   3.96         83.33               12              2.40         42.26            0.00                  40.56                 310.0           20.0               0.06                      ok
  NVDA     option         option NVDA261120C00235000       2026-10-07                   1     40     52300.0                 53200.0        13.08          13.30      236.83        234.24     last_price_stale                        NaN                unavailable                   False           900.0                   1.72         90.91               22              1.01         37.07            0.39                  24.15               17037.0         1205.0               0.01                      ok
```

## Today's Closed Trades (2026-10-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           88.46               26            1.47             14.68       1419.69                55.22         0.579          pass              0.497             35.7                           0.275                5.36              0.858                                 ok            True                  False
   CEG           90.91               33            0.78              1.64        298.89                58.54         0.578          pass              0.649             48.9                           0.520               13.62              1.473                                 ok            True                  False
  CSCO           86.96               23            0.82              0.68        117.10                34.80         0.569          pass              0.377             16.1                           0.389                9.26              1.192                                 ok            True                  False
   ADI           83.33               18            1.61              4.62        408.10                34.70         0.533          pass              0.196              0.0                           0.217                5.45              0.697                                 ok            True                  False
  ASML           80.00               30            0.69              8.67       1801.24                39.58         0.527          pass              0.408             74.0                           0.663                4.07              0.454                                 ok            True                  False
  AMGN           84.00               25            0.78              2.26        412.11                28.61         0.513          pass              0.336             26.1                           0.258                0.94             -0.206                                 ok            True                  False
  UPRO           84.62               26            1.02              1.11        154.75                30.53         0.507          pass              0.415             44.9                           0.531                2.43              0.412                                 ok            True                  False
    MU           90.62               32            0.92              7.02       1084.99                48.12         0.505          pass              0.665             61.4                           0.606               -0.24             -0.007                                 ok            True                  False
  DRAM           83.33               24            2.04              0.86         59.65                50.38         0.505          pass              0.325             30.6                           0.492               -3.18             -0.236                                 ok            True                  False
  DASH           87.50               40            0.70              0.93        190.84                42.67         0.502          pass              0.450              0.0                           0.250                1.27              0.313                                 ok            True                  False
  MSTR           91.18               34            1.42              1.53        152.72                80.80         0.615          pass              0.663             47.7                           0.567               -6.45             -0.148           downtrend_blocked_streak           False                  False
  QCOM           86.96               23            2.12              2.63        175.99                56.66         0.567          pass              0.346              5.8                           0.274              -10.76             -1.119 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008093006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008093006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008093006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008093006)

</details>
