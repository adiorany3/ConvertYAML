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
1. `AKUN-001-UNKNOWN-VLESS-WS-96MS` (url=221ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-90MS` (url=210ms, nekobox=248ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-93MS` (url=237ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-110MS` (url=250ms, nekobox=279ms, status=yes)
5. `AKUN-005-DEV-VLESS-WS-101MS` (url=229ms, nekobox=266ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-109MS` (url=308ms, nekobox=282ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-101MS` (url=243ms, nekobox=279ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=264ms, nekobox=321ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=225ms, nekobox=253ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-108MS` (url=254ms, nekobox=276ms, status=yes)
11. `AKUN-011-DEV-VLESS-WS-116MS` (url=239ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-101MS` (url=229ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-129MS` (url=247ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-141MS` (url=253ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-120MS` (url=261ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-112MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-107MS` (url=241ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-132MS` (url=277ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-95MS` (url=245ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-178MS` (url=260ms, status=HTTP 204)
22. `AKUN-022-GO-DADDY-COM-LLC-VLESS-WS-176MS` (url=285ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-115MS` (url=285ms, status=HTTP 204)
24. `AKUN-024-466688-VLESS-WS-142MS` (url=286ms, status=HTTP 204)
25. `AKUN-025-MYBB-VLESS-WS-174MS` (url=235ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
