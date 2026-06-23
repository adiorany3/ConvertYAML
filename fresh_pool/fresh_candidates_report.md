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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=212ms, nekobox=235ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=228ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-90MS` (url=210ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDWEBMANAGE-EU-FR-VLESS-WS-83MS` (url=206ms, nekobox=232ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=222ms, nekobox=253ms, status=yes)
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-98MS` (url=220ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS` (url=229ms, nekobox=203ms, status=no)
8. `AKUN-007-MEDIUM-VLESS-WS-100MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-114MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-115MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-103MS` (url=242ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-1PASSWORD-VLESS-WS-112MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=199ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-113MS` (url=230ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-128MS` (url=207ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-118MS` (url=216ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-125MS` (url=244ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-243MS` (url=519ms, status=HTTP 204)
22. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-248MS` (url=574ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-256MS` (url=547ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-273MS` (url=552ms, status=HTTP 204)
25. `AKUN-025-RS-RAPIDSEEDBOX-20190717-VLESS-WS-296MS` (url=569ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
