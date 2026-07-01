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
1. `AKUN-001-UNKNOWN-VLESS-WS-116MS` (url=326ms, nekobox=345ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-127MS` (url=270ms, nekobox=293ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-124MS` (url=274ms, nekobox=304ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-114MS` (url=290ms, nekobox=279ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-124MS` (url=295ms, nekobox=298ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-134MS` (url=279ms, nekobox=311ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-130MS` (url=281ms, nekobox=294ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-137MS` (url=251ms, nekobox=287ms, status=yes)
9. `AKUN-009-AEZA-NETWORK-VLESS-WS-143MS` (url=288ms, nekobox=273ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-147MS` (url=273ms, nekobox=282ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-122MS` (url=265ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-138MS` (url=271ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-124MS` (url=292ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-136MS` (url=248ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-120MS` (url=284ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-329MS` (url=679ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-319MS` (url=658ms, status=HTTP 204)
18. `AKUN-019-LOCAL-VLESS-WS-310MS` (url=667ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-330MS` (url=662ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-342MS` (url=654ms, status=HTTP 204)
21. `AKUN-022-COMPREND-NET-VLESS-WS-146MS` (url=257ms, status=HTTP 204)
22. `AKUN-023-COMPREND-NET-VLESS-WS-135MS` (url=248ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-354MS` (url=650ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-366MS` (url=636ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-373MS` (url=744ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
