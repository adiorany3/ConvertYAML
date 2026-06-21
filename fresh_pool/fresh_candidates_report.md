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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-84MS` (url=227ms, nekobox=241ms, status=yes)
2. `AKUN-002-104-253-175-0-1-VLESS-WS-89MS` (url=225ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS` (url=227ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=232ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=200ms, nekobox=262ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-102MS` (url=232ms, nekobox=188ms, status=no)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-84MS` (url=207ms, nekobox=192ms, status=no)
8. `AKUN-006-CLOUDFLARE-VLESS-WS-106MS`
9. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-97MS`
11. `AKUN-009-DIGITALOCEAN-VLESS-WS-114MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-114MS`
13. `AKUN-013-CLOUDWEBMANAGE-EU-FR-VLESS-WS-112MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-118MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-121MS` (url=208ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-111MS` (url=200ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-141MS` (url=229ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-89MS` (url=201ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-135MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-86MS` (url=231ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-117MS` (url=254ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-88MS` (url=203ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-245MS` (url=513ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-269MS` (url=579ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-278MS` (url=576ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
