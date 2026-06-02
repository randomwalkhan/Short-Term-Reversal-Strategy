# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:15:02 EDT`
Last processed slot: `early_entry_1015`

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

- Cash: `$33,669.25`
- Equity: `$33,669.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           95.00               20            1.36              0.85         88.74                49.60         0.629          pass              0.572             14.2                           0.181               -0.73              0.178                                 ok            True                  False
  FTNT          100.00               27            1.48              1.53        146.49                71.69         0.625          pass              0.772             65.5                           0.669               14.59              1.260                                 ok            True                  False
  MELI           91.67               24            1.91             23.16       1721.05                60.28         0.593          pass              0.569             35.1                           0.334                7.06              0.717                                 ok            True                  False
  AMGN           90.00               10            1.33              3.06        327.82                20.27         0.554          pass              0.430             36.0                           0.380                0.11              0.016                                 ok            True                  False
   CSX           86.96               23            0.70              0.22         45.76                23.46         0.507          pass              0.518             65.1                           0.316               -1.13             -0.062                                 ok            True                  False
  ROST           93.55               31            0.64              1.00        223.64                42.05         0.504          pass              0.795             81.0                           0.429                5.48              0.678                                 ok            True                  False
  AMZN           85.71               14            1.78              3.26        259.86                24.44         0.500          pass              0.327             32.5                           0.571               -3.11             -0.004                                 ok            True                  False
  INSM           50.00               12            3.98              2.95        104.76               110.78         0.672          pass              0.149             22.9                           0.457               -4.98             -0.323            downtrend_blocked_slope           False                  False
    ZS           50.00                4            7.51              8.18        152.20               157.27         0.595          pass              0.123             21.2                           0.269              -17.56             -2.744            downtrend_blocked_slope           False                  False
  SHOP           73.33               15            3.51              3.05        122.81                84.68         0.571          pass              0.191             33.4                           0.480               16.96              1.995                                 ok           False                  False
   WMT           76.92               13            1.43              1.15        114.11                32.65         0.569          pass              0.093              5.2                           0.181              -15.28             -1.713 downtrend_blocked_slope_and_streak           False                  False
  MSFT          100.00                2            2.81              9.05        456.64                28.37         0.549          pass              0.527             24.0                           0.511                5.91              0.836                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                 detail
2026-06-02T10:15:02.269482-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015 entry_candidate_skipped {"early_entry_score": 0.679, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 117.0, "option_spread_pct": 24.24, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.442}
2026-06-02T10:10:06.260122-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:05:01.451088-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T10:00:02.499087-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                             {"reason": "no_candidate"}
2026-06-02T09:20:05.650957-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                          {'saved': 92}
2026-06-01T15:10:04.135705-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-01T15:05:05.129733-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-01T15:00:02.274373-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-06-01T14:55:05.958850-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602101502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602101502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602101502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602101502)

</details>
