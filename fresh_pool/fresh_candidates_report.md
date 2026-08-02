# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-77MS` (url=235ms, nekobox=232ms, status=yes)
2. `AKUN-002-SPEEDTEST-VLESS-WS-74MS` (url=222ms, nekobox=180ms, status=no)
3. `AKUN-002-UNKNOWN-VLESS-WS-82MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-83MS` (url=226ms, nekobox=181ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS` (url=221ms, nekobox=181ms, status=no)
7. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS`
8. `AKUN-009-SPEEDTEST-VLESS-WS-93MS` (url=229ms, nekobox=179ms, status=no)
9. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS`
10. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS`
11. `AKUN-007-UNKNOWN-VLESS-WS-111MS`
12. `AKUN-008-UNKNOWN-VLESS-WS-90MS`
13. `AKUN-009-CLOUDFLARE-VLESS-WS-130MS`
14. `AKUN-010-UNKNOWN-VLESS-WS-132MS`
15. `AKUN-016-UNKNOWN-VLESS-WS-121MS` (url=257ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-136MS` (url=457ms, status=HTTP 204)
17. `AKUN-018-DEV-VLESS-WS-131MS` (url=213ms, status=HTTP 204)
18. `AKUN-019-FASTVPSUS-IPV4-VLESS-WS-140MS` (url=221ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-243MS` (url=521ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-260MS` (url=283ms, status=HTTP 204)
21. `AKUN-024-SUKARIO-VLESS-WS-417MS` (url=664ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-386MS` (url=453ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-418MS` (url=737ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-419MS` (url=734ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-527MS` (url=868ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
