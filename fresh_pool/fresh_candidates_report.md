# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-VULTR-VLESS-WS-86MS` (url=219ms, nekobox=250ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS` (url=236ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS` (url=231ms, nekobox=258ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-104MS` (url=234ms, nekobox=235ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=203ms, nekobox=241ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-102MS` (url=252ms, nekobox=231ms, status=yes)
7. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-96MS` (url=221ms, nekobox=245ms, status=yes)
8. `AKUN-008-BROADNNET-KR-VLESS-WS-104MS` (url=271ms, nekobox=259ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS` (url=239ms, nekobox=253ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-111MS` (url=235ms, nekobox=258ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-118MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-BROADNNET-KR-VLESS-WS-92MS` (url=281ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-389MS` (url=767ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-393MS` (url=788ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-405MS` (url=769ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-412MS` (url=854ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-415MS` (url=834ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-411MS` (url=882ms, status=HTTP 204)
19. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-438MS` (url=909ms, status=HTTP 204)
20. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-358MS` (url=1215ms, status=HTTP 204)
21. `AKUN-027-CLOUDFLARE-VLESS-WS-852MS` (url=1378ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
