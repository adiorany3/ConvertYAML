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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=197ms, nekobox=228ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=210ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=205ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=206ms, nekobox=247ms, status=yes)
5. `AKUN-005-ZVC-VLESS-WS-85MS` (url=228ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=221ms, nekobox=227ms, status=yes)
7. `AKUN-007-PUBLICDOMAINREGISTRY-NET-VLESS-WS-66MS` (url=228ms, nekobox=245ms, status=yes)
8. `AKUN-008-466688-VLESS-WS-97MS` (url=232ms, nekobox=246ms, status=yes)
9. `AKUN-009-NET-82-21-84-0-24-VLESS-WS-93MS` (url=226ms, nekobox=250ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS` (url=221ms, nekobox=242ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-85MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-090227-VLESS-WS-107MS` (url=206ms, status=HTTP 204)
13. `AKUN-013-1PASSWORD-VLESS-WS-96MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-76MS` (url=211ms, status=HTTP 204)
15. `AKUN-016-MYBB-VLESS-WS-115MS` (url=208ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-122MS` (url=222ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-158MS` (url=237ms, status=HTTP 204)
18. `AKUN-019-ES-FORNEX-20160629-VLESS-WS-112MS` (url=230ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-225MS` (url=517ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-220MS` (url=477ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-75MS` (url=225ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-241MS` (url=484ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-255MS` (url=526ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-221MS` (url=486ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-279MS` (url=548ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
