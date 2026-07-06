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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=195ms, nekobox=239ms, status=yes)
2. `AKUN-002-VULTR-VLESS-WS-62MS` (url=257ms, nekobox=247ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=209ms, nekobox=249ms, status=yes)
4. `AKUN-004-OVH-VLESS-WS-68MS` (url=228ms, nekobox=244ms, status=yes)
5. `AKUN-005-CHSL-HEL-VLESS-WS-72MS` (url=206ms, nekobox=268ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS` (url=202ms, nekobox=182ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS`
8. `AKUN-007-WPENG-VLESS-WS-66MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-76MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-73MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-107MS` (url=234ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-99MS` (url=206ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-106MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-107MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-116MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-105MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-MEDIUM-VLESS-WS-68MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-343MS` (url=717ms, status=HTTP 204)
21. `AKUN-021-SPEEDTEST-VLESS-WS-353MS` (url=750ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-376MS` (url=854ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-381MS` (url=799ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-388MS` (url=811ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-387MS` (url=837ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
