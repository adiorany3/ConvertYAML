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
1. `AKUN-001-MYBB-VLESS-WS-107MS` (url=266ms, nekobox=310ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-99MS` (url=271ms, nekobox=321ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-115MS` (url=312ms, nekobox=350ms, status=yes)
4. `AKUN-004-US-VLESS-WS-109MS` (url=299ms, nekobox=311ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-121MS` (url=291ms, nekobox=277ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-124MS` (url=275ms, nekobox=317ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=283ms, nekobox=313ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-122MS` (url=294ms, nekobox=321ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-118MS` (url=246ms, nekobox=297ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS` (url=279ms, nekobox=296ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-122MS` (url=290ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-133MS` (url=284ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-148MS` (url=281ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-167MS` (url=275ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-148MS` (url=287ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-134MS` (url=303ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-170MS` (url=300ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-134MS` (url=279ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=263ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-195MS` (url=360ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-279MS` (url=550ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-286MS` (url=609ms, status=HTTP 204)
23. `AKUN-024-WPENG-VLESS-WS-346MS` (url=724ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-347MS` (url=621ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-353MS` (url=731ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
