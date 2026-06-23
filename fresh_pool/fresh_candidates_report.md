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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-101MS` (url=341ms, nekobox=339ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-119MS` (url=335ms, nekobox=273ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-129MS` (url=338ms, nekobox=280ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-134MS` (url=349ms, nekobox=272ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=243ms, nekobox=282ms, status=yes)
6. `AKUN-006-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-127MS` (url=241ms, nekobox=295ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-126MS` (url=330ms, nekobox=281ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-105MS` (url=327ms, nekobox=365ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-127MS` (url=237ms, nekobox=323ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-114MS` (url=248ms, nekobox=279ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-122MS` (url=310ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-135MS` (url=265ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-108MS` (url=245ms, status=HTTP 204)
14. `AKUN-014-CLOUDWEBMANAGE-EU-FR-VLESS-WS-113MS` (url=327ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-140MS` (url=256ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-125MS` (url=241ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-114MS` (url=261ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-301MS` (url=670ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-122MS` (url=267ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-355MS` (url=727ms, status=HTTP 204)
21. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-396MS` (url=702ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-354MS` (url=734ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-313MS` (url=714ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-356MS` (url=660ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-570MS` (url=804ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
