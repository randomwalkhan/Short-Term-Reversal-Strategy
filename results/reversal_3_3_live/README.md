# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:05:05 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$28,317.75`
- Equity: `$28,317.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  INTC           96.43               28            1.50              1.25        118.43               113.85         0.730          pass              0.792             66.4                           0.855                6.90             -0.588                      ok            True                  False
  NXPI           81.82               33            0.63              1.38        309.56                91.65         0.714          pass              0.493             73.3                           0.811                6.19              0.315                      ok            True                  False
  FTNT          100.00               38            0.72              0.66        129.72                70.74         0.615          pass              0.846             66.0                           0.584               19.53              1.790                      ok            True                   True
  SBUX           91.67               12            1.52              1.13        106.02                31.64         0.586          pass              0.495             37.3                           0.378                1.19              0.185                      ok            True                  False
  PAYX           94.44               18            0.73              0.48         94.71                29.35         0.558          pass              0.698             68.1                           0.760                1.25              0.248                      ok            True                  False
  MNST           83.87               31            0.71              0.43         86.70                49.77         0.549          pass              0.557             86.2                           0.688               13.55              0.668                      ok            True                  False
   ADP           93.33               30            0.86              1.32        220.12                38.26         0.532          pass              0.703             53.6                           0.633                2.20              0.440                      ok            True                  False
    ZS           85.00               20            2.25              2.75        173.27                63.59         0.518          pass              0.332             26.6                           0.258               11.60              1.816                      ok            True                  False
  ISRG           85.71               14            2.18              6.84        446.10                35.82         0.512          pass              0.316             28.7                           0.328               -3.14             -0.007                      ok            True                  False
   TXN           90.91               22            1.17              2.51        303.81                69.08         0.506          pass              0.564             47.5                           0.580                5.63              0.522                      ok            True                  False
  INSM           76.32               38            0.82              0.62        107.65               110.82         0.741          pass              0.365             34.8                           0.276                1.93              0.191                      ok           False                  False
 CMCSA           86.67               30            0.56              0.10         24.84                59.59         0.617          pass              0.542             56.3                           0.576               -5.72             -0.372 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T10:05:05.076526-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:05:05.076526-04:00 early_entry_1005 entry_candidate_skipped  {"early_entry_score": 0.71, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 38.0, "option_spread_pct": 29.21, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.483}
2026-05-21T10:05:05.076526-04:00 early_entry_1005 entry_candidate_skipped                  {"early_entry_score": 0.846, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 608.0, "option_spread_pct": 30.23, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.615}
2026-05-21T10:00:05.181059-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:00:05.181059-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.679, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 13.0, "option_spread_pct": 19.61, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.487}
2026-05-21T10:00:05.181059-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.726, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 36.96, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.571}
2026-05-21T09:20:03.993328-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                           {'saved': 92}
2026-05-20T15:10:05.258354-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-20T15:05:01.057777-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-05-20T15:00:06.267185-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521100505)

</details>
