# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-70MS` (url=248ms, nekobox=268ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-87MS` (url=256ms, nekobox=296ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=239ms, nekobox=263ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-101MS` (url=258ms, nekobox=303ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-105MS` (url=249ms, nekobox=278ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=253ms, nekobox=306ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-103MS` (url=310ms, nekobox=386ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-97MS` (url=252ms, nekobox=185ms, status=no)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-106MS` (url=254ms, nekobox=183ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-115MS`
11. `AKUN-009-OPENAI-VLESS-WS-98MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-286MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-300MS` (url=630ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-321MS` (url=2486ms, status=HTTP 204)
15. `AKUN-018-CLOUDFLARE-VLESS-WS-483MS` (url=734ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-104MS` (url=302ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-314MS` (url=653ms, status=HTTP 204)
18. `AKUN-022-UNKNOWN-VLESS-WS-489MS` (url=644ms, status=HTTP 204)
19. `AKUN-023-UNKNOWN-VLESS-WS-494MS` (url=801ms, status=HTTP 204)
20. `AKUN-026-CLOUDFLARE-VLESS-WS-312MS` (url=623ms, status=HTTP 204)
21. `AKUN-028-UNKNOWN-VLESS-WS-564MS` (url=843ms, status=HTTP 204)
22. `AKUN-033-CLOUDFLARE-VLESS-WS-311MS` (url=4668ms, status=HTTP 204)
23. `AKUN-035-CLOUDFLARE-VLESS-WS-718MS` (url=2611ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
