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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-73MS` (url=212ms, nekobox=257ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=224ms, nekobox=241ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=232ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS` (url=230ms, nekobox=232ms, status=yes)
5. `AKUN-005-DIGITALOCEAN-VLESS-WS-82MS` (url=231ms, nekobox=262ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-80MS` (url=206ms, nekobox=246ms, status=yes)
7. `AKUN-007-MYBB-VLESS-WS-85MS` (url=207ms, nekobox=258ms, status=yes)
8. `AKUN-008-466688-VLESS-WS-73MS` (url=210ms, nekobox=261ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS` (url=226ms, nekobox=262ms, status=yes)
10. `AKUN-010-US-VLESS-WS-85MS` (url=201ms, nekobox=251ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-82MS` (url=295ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-85MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-1PASSWORD-VLESS-WS-103MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-83MS` (url=204ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-85MS` (url=234ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-78MS` (url=217ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-117MS` (url=225ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-141MS` (url=235ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-112MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-CLOUDWEBMANAGE-EU-FR-VLESS-WS-117MS` (url=230ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-114MS` (url=332ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-104MS` (url=197ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-356MS` (url=723ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-371MS` (url=781ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
