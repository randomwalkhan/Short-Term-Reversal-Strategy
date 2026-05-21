# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-21 10:10:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  INTC           95.24               21            2.42              2.02        118.10               113.85         0.719            pass              0.682             45.7                           0.556                5.89             -0.631                      ok            True                  False
  NXPI           81.82               33            0.59              1.27        309.60                91.65         0.717            pass              0.499             75.3                           0.835                6.24              0.317                      ok            True                  False
  FTNT          100.00               34            0.83              0.76        129.68                70.74         0.634            pass              0.806             60.9                           0.608               19.40              1.785                      ok            True                   True
  PAYX           94.74               19            0.66              0.44         94.73                29.35         0.556            pass              0.721             70.8                           0.809                1.32              0.251                      ok            True                  False
 GOOGL           83.33               24            1.16              3.15        387.56                41.00         0.555            pass              0.309             23.6                           0.269               -3.41             -0.243                      ok            True                  False
  MNST           83.87               31            0.69              0.42         86.70                49.77         0.550            pass              0.558             86.5                           0.689               13.57              0.669                      ok            True                  False
   ADP           93.33               30            0.81              1.25        220.16                38.26         0.536            pass              0.711             56.3                           0.688                2.25              0.442                      ok            True                  False
  ISRG           86.67               15            2.07              6.49        446.25                35.82         0.513            pass              0.359             32.3                           0.538               -3.03             -0.002                      ok            True                  False
   TXN           90.91               22            1.21              2.58        303.78                69.08         0.504            pass              0.559             46.0                           0.583                5.60              0.521                      ok            True                  False
  FAST           90.91               22            1.05              0.32         43.54                21.35         0.503            pass              0.542             40.3                           0.623               -2.57             -0.124                      ok            True                  False
    ZS           87.10               31            1.40              1.72        173.71                63.59         0.500 below_threshold              0.542             54.2                           0.526               12.57              1.855                      ok            True                  False
  CHTR           88.10               42            0.41              0.42        144.43               113.96         0.764            pass              0.727             78.2                           0.766              -10.13             -0.936 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                  detail
2026-05-21T10:10:05.107052-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped                  {"early_entry_score": 0.691, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1903.0, "option_spread_pct": 73.17, "option_volume": 14.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.46}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped                   {"early_entry_score": 0.694, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 493.0, "option_spread_pct": 20.94, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MAR", "timing_score": 0.414}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped {"early_entry_score": 0.718, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 38.0, "option_spread_pct": 29.21, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.487}
2026-05-21T10:10:05.107052-04:00 early_entry_1010 entry_candidate_skipped                  {"early_entry_score": 0.806, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 608.0, "option_spread_pct": 30.23, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.634}
2026-05-21T10:05:05.076526-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-21T10:05:05.076526-04:00 early_entry_1005 entry_candidate_skipped  {"early_entry_score": 0.71, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 38.0, "option_spread_pct": 29.21, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTSH", "timing_score": 0.483}
2026-05-21T10:05:05.076526-04:00 early_entry_1005 entry_candidate_skipped                  {"early_entry_score": 0.846, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 608.0, "option_spread_pct": 30.23, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.615}
2026-05-21T10:00:05.181059-04:00 early_entry_1000 entry_candidate_skipped {"early_entry_score": 0.726, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 36.96, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.571}
2026-05-21T10:00:05.181059-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                  {"reason": "no_trade_after_option_and_timing_filters"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260521101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260521101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260521101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260521101005)

</details>
