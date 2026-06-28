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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-113MS` (url=291ms, nekobox=288ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-121MS` (url=283ms, nekobox=341ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-124MS` (url=287ms, nekobox=326ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-131MS` (url=281ms, nekobox=339ms, status=yes)
5. `AKUN-005-CLOUDWEBMANAGE-EU-FR-VLESS-WS-135MS` (url=266ms, nekobox=334ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-123MS` (url=351ms, nekobox=310ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-151MS` (url=280ms, nekobox=323ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-139MS` (url=300ms, nekobox=302ms, status=yes)
9. `AKUN-009-VULTR-VLESS-WS-114MS` (url=262ms, nekobox=312ms, status=yes)
10. `AKUN-010-DE-XTOM-20210903-VLESS-WS-118MS` (url=286ms, nekobox=287ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-152MS` (url=248ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-125MS` (url=279ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-137MS` (url=302ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=266ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-118MS` (url=293ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-124MS` (url=311ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-131MS` (url=369ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-127MS` (url=294ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-170MS` (url=252ms, status=HTTP 204)
20. `AKUN-020-CONFLU-VLESS-WS-329MS` (url=608ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-344MS` (url=718ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-341MS` (url=609ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-334MS` (url=696ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-259MS` (url=449ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-340MS` (url=722ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
