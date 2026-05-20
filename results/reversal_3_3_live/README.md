# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 10:21:54 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$26,462.75`
- Equity: `$26,462.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX           94.12               17            0.75              0.49         94.27                29.36         0.557            pass              0.709             76.6                           0.759                3.94              0.222                                 ok            True                  False
   KDP           88.89               27            0.83              0.17         28.78                34.80         0.527            pass              0.566             54.3                           0.304                0.18              0.118                                 ok            True                  False
  ADSK           88.24               17            1.66              2.84        242.94                38.52         0.521            pass              0.507             63.0                           0.778               -1.23             -0.168                                 ok            True                  False
  FTNT          100.00               42            0.47              0.42        127.46                70.74         0.609            pass              0.885             74.7                           0.741               41.23              2.634                                 ok           False                  False
  TEAM           90.62               32            2.41              1.46         85.99               114.61         0.594            pass              0.648             52.7                           0.690               -4.81             -0.565 downtrend_blocked_slope_and_streak           False                  False
  CTSH           81.25               16            1.87              0.66         50.60                50.98         0.520            pass              0.280             51.4                           0.640               -2.04             -0.251           downtrend_blocked_streak           False                  False
   WMT           85.71                7            1.94              1.83        133.42                20.68         0.516            pass              0.331             42.4                           0.268                1.35              0.307                                 ok           False                  False
   TRI           75.00               12            2.44              1.49         86.71                57.28         0.497 below_threshold              0.208             48.4                           0.644               -7.12             -0.893 downtrend_blocked_slope_and_streak           False                  False
  TMUS           85.19               27            1.23              1.67        192.71                36.70         0.493 below_threshold              0.392             30.4                           0.232               -1.10             -0.186                                 ok           False                  False
  SNPS           96.67               30            1.17              4.03        492.14                41.71         0.490 below_threshold              0.796             71.3                           0.778               -3.23             -0.384 downtrend_blocked_slope_and_streak           False                  False
  META           80.00               40            0.05              0.23        602.51                37.13         0.487 below_threshold              0.528             93.1                           0.644               -1.73             -0.088           downtrend_blocked_streak           False                  False
  MSFT           84.62               26            0.95              2.77        416.23                29.51         0.486 below_threshold              0.384             35.3                           0.382               -0.12              0.064                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                         detail
2026-05-20T10:21:54.079183-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                         {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-20T10:21:54.079183-04:00 early_entry_1020 entry_candidate_skipped         {"early_entry_score": 0.683, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 46.51, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTAS", "timing_score": 0.458}
2026-05-20T10:21:54.079183-04:00 early_entry_1020 entry_candidate_skipped                   {"early_entry_score": 0.801, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 29.0, "option_spread_pct": 26.59, "option_volume": 20.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.484}
2026-05-20T10:05:07.673831-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                     {"reason": "no_candidate"}
2026-05-20T10:03:13.062601-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                         {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-20T10:03:13.062601-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.801, "option_liquidity_status": "low_open_interest,no_two_sided_quote,wide_spread", "option_open_interest": 29.0, "option_spread_pct": null, "option_volume": 20.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.484}
2026-05-20T10:03:13.062601-04:00 early_entry_1000 entry_candidate_skipped          {"early_entry_score": 0.821, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 15.38, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "TTWO", "timing_score": 0.44}
2026-05-20T09:18:59.431991-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                  {'saved': 92}
2026-05-19T15:10:04.056831-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-05-19T15:05:05.027114-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520102154)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520102154)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520102154)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520102154)

</details>
